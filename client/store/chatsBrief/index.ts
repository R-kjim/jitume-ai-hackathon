import { createSlice } from "@reduxjs/toolkit";
import { ChatBriefState } from "../types";

const initialState: ChatBriefState = {
    briefs: null,
    briefsError:null,
    briefsLoading: true
}

const briefsSlice = createSlice({
    name:"briefs",
    initialState,
    reducers: {}
})

export default briefsSlice.reducer;