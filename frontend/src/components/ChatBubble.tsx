import React from 'react';

interface Props {
  message: string;
  sender: 'user' | 'bot';
}

export const ChatBubble: React.FC<Props> = ({ message, sender }) => {
  if (!message || typeof message !== 'string' || !message.trim()) return null;
  const isUser = sender === 'user';

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4`}>
      <div className={`flex items-end gap-2 max-w-[75%]`}>
        {!isUser && (
          <img
            src="/nittany-bot.png"
            alt="Nittany Bot"
            className="w-13 h-14 rounded-md"
          />
        )}
        <div
          className={`px-5 py-3 rounded-2xl shadow-md text-[20px] leading-relaxed ${
            isUser
              ? 'bg-[#002D72] text-white'
              : 'bg-white text-[#1A1B1C] border border-gray-200'
          }`}
        >
          {message}
        </div>
      </div>
    </div>
  );
};
