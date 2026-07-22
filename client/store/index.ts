import { configureStore, combineReducers } from "@reduxjs/toolkit";
import chatBriefsReducer from "@/store/chatsBrief/index";
// import userReducer from "@/store/slices/auth/index";

import { persistStore, persistReducer } from "redux-persist";
import storage from "redux-persist/lib/storage";
import {
  FLUSH,
  REHYDRATE,
  PAUSE,
  PERSIST,
  PURGE,
  REGISTER,
} from "redux-persist";

const userPersistConfig = {
  key: "user",
  storage,
  whitelist: ["user", "notifications"],
};

const rootReducer = combineReducers({
  // user: persistReducer(userPersistConfig, userReducer),
  chatBriefs: chatBriefsReducer,
});

export const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
      },
    }),
  devTools: process.env.NODE_ENV !== "production",
});

export const persistor = persistStore(store);

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;