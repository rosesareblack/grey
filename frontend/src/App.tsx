import { useState } from "react";
import "./App.css";
type Message = { role: "user" | "assistant"; content: string };
function App() {
const [input, setInput] = useState("");
const [msgs, setMsgs] = useState<Message[]>([]);
const send = async () => {
if (!input.trim()) return;
const body = {
messages: [...msgs, { role: "user", content: input }],
temperature: 0.7,
max_tokens: 1024,
stream: false,
};
setInput("");
setMsgs((m) => [...m, { role: "user", content: input }]);
const res = await fetch("/v1/chat/completions", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify(body),
});
const json = await res.json();
const reply = json.choices[0].message.content;
setMsgs((m) => [...m, { role: "assistant", content: reply }]);
};
return (
<div className="chat"><div className="screen"><div key={i} className={m.role}><b> {m.content}

))}

<div className="bar"><button onClick={send}>


);
}
export default App;
Build static files:
cd frontend
npm i
npm run build      # creates build/ folder
