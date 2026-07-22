"use client";

import React, { useEffect, useState } from "react";
import { useWorkflowStore } from "../store/useWorkflowStore";


const API_URL =
  process.env.NEXT_PUBLIC_API_URL ||
  "http://127.0.0.1:8000";


export const Sidebar: React.FC = () => {


  const {
    searchQuery,
    setSearchQuery,
    addWorkflow,
  } = useWorkflowStore();



  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");



  // Store API data
  const [conversationsList, setConversationsList] =
    useState<any[]>([]);



  useEffect(() => {


    const fetchConversations = async () => {


      setLoading(true);
      setError("");

      try {


        const response = await fetch(
          `${API_URL}/api/conversations/`
        );



        if (!response.ok) {

          throw new Error(
            `API Error ${response.status}`
          );

        }



        const data = await response.json();



        console.log(
          "Conversations:",
          data
        );



        setConversationsList(data);



      } catch(error:any){


        console.error(error);

        setError(error.message);



      } finally {


        setLoading(false);

      }


    };


    fetchConversations();


  },[]);





  // Search filter

  const filteredConversations =
    conversationsList.filter(
      (conversation:any)=>

        conversation.speaker_label
        ?.toLowerCase()
        .includes(
          searchQuery.toLowerCase()
        )

        ||

        conversation.message
        ?.toLowerCase()
        .includes(
          searchQuery.toLowerCase()
        )

    );

  const startMeeting = async () => {

  const platform = window.prompt(
    "Choose platform: Google Meet, Zoom, Microsoft Teams",
    "Google Meet"
  );


  if (!platform) return;



  try {


    const response = await fetch(
      `${API_URL}/api/meetings/`,
      {
        method:"POST",

        headers:{
          "Content-Type":"application/json"
        },


        body:JSON.stringify({

          title:"New Client Consultation",

          client_name:"New Client",

          platform:platform,

          meeting_link:null

        })

      }
    );



    if(!response.ok){

      throw new Error(
        "Failed to create meeting"
      );

    }



    const meeting =
      await response.json();



    console.log(
      "Meeting created:",
      meeting
    );



    // Open meeting URL if generated

    if(meeting.meeting_link){

      window.open(
        meeting.meeting_link,
        "_blank"
      );

    }



  } catch(error:any){

    console.error(error);

    alert(
      error.message
    );

  }


};







return (

<aside
className="
w-80 h-full
bg-[#121318]
border-r border-gray-800
flex flex-col
text-gray-300
"
>



{/* Header */}

<div
className="
p-4
border-b border-gray-800
"
>

<div
className="
flex items-center gap-3
"
>

<div
className="
flex h-8 w-8
items-center justify-center
rounded bg-blue-600
"
>
🤖
</div>


<h2
className="
text-lg font-bold text-white
"
>
JITUME AI
</h2>


</div>

</div>





{/* New Workflow */}

<div className="p-3">

<button

onClick={startMeeting}

className="
w-full
rounded-lg
bg-blue-600
py-2
text-sm
font-semibold
hover:bg-blue-700
"

>

+ New Client Workflow

</button>

</div>







{/* Search */}

<div className="px-3 pb-3">


<input

type="text"

placeholder="Search conversations..."

value={searchQuery}

onChange={(e)=>
setSearchQuery(e.target.value)
}


className="
w-full
rounded-lg
border border-gray-700
bg-[#0d0e12]
px-3 py-2
text-sm
text-white
outline-none
focus:border-blue-500
"

/>


</div>






{/* Conversations */}

<div
className="
flex-1
overflow-y-auto
px-3 py-4
"
>


<h3
className="
mb-3
text-xs
font-bold
uppercase
text-gray-500
"
>
Recent Conversations
</h3>




{
loading &&

<p className="text-blue-400 text-sm">
Loading conversations...
</p>

}




{
error &&

<p className="text-red-400 text-sm">
{error}
</p>

}






{
filteredConversations.map(
(conversation:any)=>(


<div

key={conversation.id}

className="
mb-2
rounded-lg
border border-gray-800
bg-[#181a20]
p-3
hover:bg-gray-800
cursor-pointer
"

>



<h4
className="
font-semibold
text-white
"
>

{
conversation.speaker_label ||
conversation.speaker
}

</h4>




<p
className="
text-xs text-gray-400
"
>

{
conversation.message?.substring(
0,
60
)
}

...

</p>





<span
className="
mt-2
inline-block
rounded
bg-blue-900/30
px-2 py-1
text-[10px]
uppercase
text-blue-400
"
>

{
conversation.status
}

</span>






<p
className="
text-[10px]
text-gray-500
mt-2
"
>

{
new Date(
conversation.timestamp
).toLocaleString()
}

</p>






</div>


)

)

}





</div>



</aside>


);


};
