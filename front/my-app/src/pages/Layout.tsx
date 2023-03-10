import { useEffect } from "react";
import { useSelector } from "react-redux";
import { Outlet, Link } from "react-router-dom";
import { useAppDispatch, useAppSelector } from "../app/hooks";
import { isloggedoff, islooged, refreshAsync, selectlooged, selectUser } from "../features/login/loginSlice";
import "./layout.css"



const Layout = () => {
    const dispatch = useAppDispatch();
    const token = JSON.parse(localStorage.getItem('token') as string);
    console.log(token)
   
    const accessToken = token?.access
    useEffect(() => {
     if (accessToken){
       dispatch(islooged())
   
     }
     if (accessToken == null) {
        dispatch (isloggedoff()) 

     }
   
    },[]);

    const logged = useAppSelector(selectlooged);
    console.log (logged)

    const currentUser: string = useSelector(selectUser)

    return (
        <>
            <div style={{}}>
                <nav className="navigator">
                    <Link className="navBarLink mainLogo" to="/">
                        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" className="bi bi-asterisk" viewBox="0 0 16 16">
                            <path d="M8 0a1 1 0 0 1 1 1v5.268l4.562-2.634a1 1 0 1 1 1 1.732L10 8l4.562 2.634a1 1 0 1 1-1 1.732L9 9.732V15a1 1 0 1 1-2 0V9.732l-4.562 2.634a1 1 0 1 1-1-1.732L6 8 1.438 5.366a1 1 0 0 1 1-1.732L7 6.268V1a1 1 0 0 1 1-1z" />
                        </svg>
                        StarStore
                    </Link>
                    <input className="searchBar" placeholder="search anything at StarStore" />
                    <div className=" dropDownBtn">
                        <Link className="navBarLink" to="/login">
                            <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" className="bi bi-person-circle" viewBox="0 0 16 16">
                                <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" />
                                <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z" />
                            </svg>
                            {logged ? " Hi " + currentUser : "Account"}
                        </Link>
                        {logged && <div className="dropContent">
                            <Link className="navBarLink " to="/logout">Logout</Link></div>}
                    </div>
                    <Link className="navBarLink" to="/cart">
                        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" className="bi bi-cart" viewBox="0 0 16 16">
                            <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 13 12H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM3.102 4l1.313 7h8.17l1.313-7H3.102zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" />
                        </svg>
                        MyCart</Link>
                </nav>
                <br />
                <Outlet />
            </div>
        </>
    )
};



export default Layout;
