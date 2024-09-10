import { useEffect, useState } from "react"
import "./App.css" 
import Card from "./components/Card.jsx"
import Model from "./components/model/Model.jsx"

function App() {
  const [users,setUsers]=useState([])
  const [ismodelopen,setIsmodelopen]=useState(false)


  useEffect(()=>{
      const getUsers = async () =>{
        try{
          const res = await fetch('http://127.0.0.1:5000/api/friends')
          const data =await res.json();
          console.log(data);
          if(!res.ok){
            throw new Error(data.error);
          }
          setUsers(data)
        }catch(error){
          console.error(error);
        }finally{

        }
      } 
      getUsers();
  },[]
  )
  
  //open the model
  function addfriend(){
    setIsmodelopen(true);
    // setIsmodelopen(prevState => !prevState);
  }

  return (
    <>
        <div className="title">
          My Friends
          <button onClick={addfriend}>Add Friend</button>
        </div>
        <div className="cards">
          {users.map((user) => (
              <Card key={user.id} user={user} />
          )
          )}
        </div>

        
        {ismodelopen && <Model /> }

    </>
  )
}

export default App
