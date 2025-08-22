import React, { useState } from 'react';
import { ChatBubble } from '../components/ChatBubble';
import { ChatInput } from '../components/ChatInput';

export default function ChatPage() {
    const [messages, setMessages] = useState<{ text: string; sender: 'user' | 'ai' }[]>([]);

    const handleSend = async (message: { text: string; sender: 'user' | 'ai' }) => {
    console.log("🟢 handleSend called with:", message);
    setMessages((prev) => [...prev, message]);

try {
  const response = await fetch('http://localhost:8000/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ question: message.text }),
  });

  const data = await response.json();

  setMessages((prev) => [
    ...prev,
    { text: data.answer, sender: 'ai' }, // assuming your backend responds with { reply: "..." }
  ]);
} catch (error) {
  console.error('Error talking to backend:', error);
  setMessages((prev) => [
    ...prev,
    { text: "Sorry, something went wrong!", sender: 'ai' },
  ]);
}
};

return (
  <div className="flex flex-col h-screen">
    {/* Fixed Penn State Header */}
    <div className="w-full bg-[#002D72] py-4 px-6 flex items-center shadow z-10">
      <img src="/pennstate-logo.png" alt="Penn State Logo" className="h-18 w-auto" />
    </div>

    {/* Scrollable Chat + Input */}
    <div className="flex flex-col flex-1 overflow-y-auto bg-white">
      <div className="flex-1 p-4 overflow-y-auto pb-32">
        {messages.map((m, i) => (
          <ChatBubble key={i} message={m.text} sender={m.sender} />
        ))}
      </div>

      <div className="border-t p-4">
        <ChatInput onSend={handleSend} />
      </div>
    </div>
  </div>
);
}
