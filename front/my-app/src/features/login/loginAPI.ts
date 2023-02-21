import axios from "axios";
import {SERVER} from "../globalVar"

// export function userFetch(creds:any) {
//     return new Promise<{ data: any }>((resolve,reject) =>
//       axios.post(SERVER+ "login/", { username:creds.username, password:creds.password })
//         .then((res) => localStorage.setItem("token"),JSON. res.data ))      
//         .catch((error)=>reject(error.data))
        

//     );
//   }

  export const userFetch = async (creds: any) => {
    const response = await axios.post(SERVER+ "login/", { username:creds.username, password:creds.password })
  
    if (response.data) {
      localStorage.setItem("token", JSON.stringify(response.data));
    }
    console.log(response.data)
    return response.data;
  };


export function userRegister(creds:any) {
  return new Promise<{ data: any }>((resolve) =>
    axios
      .post(SERVER+ "register/", { username:creds.username, password:creds.password })
      .then((res) => resolve({ data: res.data }))
      .catch((error)=>console.log(error))
  );
}
  
  export function refreshUser(refresh:any) {
    return new Promise<{ data: any }>((resolve) =>
      axios
        .post(SERVER+ "refresh/", { refresh })
        .then((res) => resolve({ data: res.data }))
    );
  }

  export function logoutUser() {
    localStorage.removeItem("token");
  }
