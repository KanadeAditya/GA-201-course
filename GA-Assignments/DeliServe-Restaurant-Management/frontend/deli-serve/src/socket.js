import io from "socket.io-client";

const socket = io("http://localhost:5050"); // Replace with your Socket server URL

export default socket