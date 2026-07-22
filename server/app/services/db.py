from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type, Any, Dict, AnyStr, Optional
from sqlalchemy import asc, desc, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import selectinload, class_mapper


def get_recursive_selectinloads(model, depth):
    if depth == 0:
        return []
    options = []
    for rel in class_mapper(model).relationships:
        rel_attr = getattr(model, rel.key)
        loader = selectinload(rel_attr)
        nested = get_recursive_selectinloads(rel.mapper.class_, depth - 1)
        for n in nested:
            loader = loader.options(n)
        options.append(loader)
    return options

def _filter_model_fields(model: Type, data: Dict[str, Any]) -> Dict[str, Any]:
    valid_fields = {col.key for col in model.__table__.columns}
    return {k: v for k, v in data.items() if k in valid_fields}

class GetCreateUpdateDelete:

    @staticmethod
    async def get_one(
            db:AsyncSession,
            model:Type,
            filters:Optional[Dict[AnyStr,Any]] = None,
            relationships: bool = False,
            return_is_deleted : bool = False,
            depth:int =2
    ) -> Optional[Any]:
        stmt = select(model)
        if relationships:
            stmt = stmt.options(*get_recursive_selectinloads(model=model, depth=depth))

        if return_is_deleted:
            stmt = stmt.where(getattr(model,"is_deleted") == True)
        if filters:
            for key, value in filters.items():
                stmt= stmt.where(getattr(model,key) == value)
        
        result= await db.execute(stmt)
        return result.scalars().first()
    
    @staticmethod
    async def get_all(
        db: AsyncSession,
        model: Type,
        filters: Optional[Dict[AnyStr, Any]]=None,
        relationship = False,
        order_by: Optional[str] = None,
        order_dir: str = "asc",
    ) -> Optional[Any]:
        stmt = select(model)

        if relationship:
            relationships = [rel.key for rel in class_mapper(model).relationships]
            for rel in relationships:
                stmt = stmt.options(selectinload(getattr(model, rel)))

        if filters:
            for key, value in filters.items():
                stmt= stmt.where(getattr(model, key) == value)
        if order_by:
            order_column = getattr(model, order_by)
            if order_dir.lower() == "desc":
                stmt = stmt.order_by(desc(order_column))
            else:
                stmt = stmt.order_by(asc(order_column))

        result = await db.execute(stmt)
        return result.scalars().all()
    
    @staticmethod
    async def create_one(
        db:AsyncSession,
        model: Type,
        data:Dict[ AnyStr, Any],
        flush:bool = True
    ) -> Any:
        data=_filter_model_fields(model=model, data=data)
        instance = model(**data)
        db.add(instance=instance)

        if flush:
            await db.flush()
        
        return instance

    @staticmethod
    async def delete_one(
        db: AsyncSession,
        model: Type,
        filters: Dict [ AnyStr, Any]
    ):
        stmt = select(model)
        for entry, value in filters.items():
            stmt = stmt.where(getattr(model,entry)== value)
        result = await db.execute(stmt)
        res = result.scalars().first()
        await db.delete(res)
        return
    
    @staticmethod
    async def update_one(
        db: AsyncSession,
        model: Type,
        obj_id: Any,
        data: Dict[AnyStr, Any],
        id_field: str = "id",
        flush: bool = True
    ) -> Any:
        # Fetch existing instance
        stmt = select(model).where(getattr(model, id_field) == obj_id)
        result = await db.execute(stmt)
        instance = result.scalars().first()

        if not instance:
            raise NoResultFound(f"{model.__name__} with {id_field}={obj_id} not found.")

        filtered_data = _filter_model_fields(model=model, data=data)
        for key, value in filtered_data.items():
            if value:
                setattr(instance, key, value)

        if flush:
            await db.flush()

        return instance
    
    @staticmethod
    async def conditional_get_all(
        db: AsyncSession,
        model: Type,
        filters: Optional[Dict[AnyStr, Any]]=None,
        relationship = False,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        order_by: Optional[str] = None,
        order_dir: str = "asc",
        search_field: Optional[str] = None,
        search_word: Optional[str] = None
    ) -> Optional[Any]:
        stmt = select(model)

        # if relationship:
        #     relationships = [rel.key for rel in class_mapper(model).relationships]
        #     for rel in relationships:
        #         stmt = stmt.options(selectinload(getattr(model, rel)))

        if relationship:
            for option in get_recursive_selectinloads(model, depth=2):
                stmt = stmt.options(option)

        if filters:
            for key, value in filters.items():
                stmt= stmt.where(getattr(model, key) == value)
        
        # Apply search filter (case-insensitive partial match)
        if search_field and search_word:
            stmt = stmt.where(getattr(model, search_field).ilike(f"%{search_word}%"))

        # Apply ordering
        if order_by:
            order_column = getattr(model, order_by)
            if order_dir.lower() == "desc":
                stmt = stmt.order_by(desc(order_column))
            else:
                stmt = stmt.order_by(asc(order_column))

        # Apply pagination
        if offset is not None:
            stmt = stmt.offset(offset)
        if limit is not None:
            stmt = stmt.limit(limit)
            
        result = await db.execute(stmt)
        return result.scalars().all()

get_create_update_delete = GetCreateUpdateDelete()