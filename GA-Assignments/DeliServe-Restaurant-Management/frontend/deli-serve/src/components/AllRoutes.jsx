import React from "react";
import { Routes, Route } from "react-router-dom";

import Admin from "../pages/Admin";
import Home from "../pages/Home";
import User from "../pages/User";

function AllRoutes() {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/user" element={<User />} />
            <Route path="/admin" element={<Admin />} />
        </Routes>
    );
}

export default AllRoutes;
