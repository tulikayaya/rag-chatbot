import React, { useState, useRef, useEffect } from 'react';

interface Props {
  onSend: (msg: { sender: string; text: string }) => void;
}

export const ChatInput: React.FC<Props> = ({ onSend }) => {
  const [text, setText] = useState('');
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleSend = () => {
    if (!text.trim()) return;

    onSend({ sender: 'user', text });
    setText('');
  };

  useEffect(() => {
    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = 'auto';
      textarea.style.height = `${Math.min(textarea.scrollHeight, 200)}px`;
    }
  }, [text]);

  return (
    <div className="flex items-end gap-2">
      <textarea
        ref={textareaRef}
        rows={1}
        aria-label="Chat message"
        className="flex-1 resize-none overflow-y-auto border-2 border-[#002D72] rounded-xl px-4 py-3 text-[20px] font-[Times_New_Roman] text-[#1A1B1C] leading-relaxed focus:outline-none focus:ring-2 focus:ring-[#002D72] focus:border-[#002D72] max-h-[200px]"
        placeholder="Type your message..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSend();
          }
        }}
      />
      <button
        onClick={handleSend}
        className="flex items-center justify-center w-14 h-14 rounded-full bg-[#002D72] hover:bg-blue-800 transition"
        aria-label="Send message"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="white"
          viewBox="0 0 24 24"
          strokeWidth={3}
          stroke="white"
          className="w-8 h-8 text-white"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M5 12h14m0 0l-6-6m6 6l-6 6"
          />
        </svg>
      </button>
    </div>
  );
};
