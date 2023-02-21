import axios from "axios";
import { SERVER } from "../globalVar";
export function prodFetch(creds:any) {
    console.log(creds);
    return new Promise<{ data: any }>((resolve) =>
      axios
        .post(SERVER + "upload_image/", creds, {headers:{"content-type": "multipart/form-data",
      } })
        .then((res) => resolve({ data: res.data }))
    );
  }
  
  export function rmv_prod(creds:any) {
    return new Promise<{ data: any }>((resolve) =>
    axios.delete(SERVER + `myProducts/${creds}`)
        .then((res) => resolve({ data: res.data }))
    );
  }
