// src/components/CommentSection.jsx
import { useState } from "react";

export default function CommentSection({ eventId }) {
  const [comments, setComments] = useState([
    { id: 1, user: "Alice", content: "Excited for this event!" },
    { id: 2, user: "Bob", content: "Can't wait to attend!" },
  ]);

  const [newComment, setNewComment] = useState("");

  const handleAddComment = () => {
    if (newComment.trim() === "") return;
    const comment = {
      id: comments.length + 1,
      user: "CurrentUser",
      content: newComment,
    };
    setComments([comment, ...comments]);
    setNewComment("");
  };

  return (
    <div className="mt-4">
      <h3 className="text-sm font-semibold text-gray-700 mb-2">Comments</h3>
      <div className="flex flex-col gap-2 max-h-48 overflow-y-auto">
        {comments.map((c) => (
          <div
            key={c.id}
            className="bg-gray-100 rounded-lg p-2 text-gray-800 text-sm"
          >
            <span className="font-semibold">{c.user}:</span> {c.content}
          </div>
        ))}
      </div>
      <div className="mt-2 flex gap-2">
        <input
          type="text"
          placeholder="Add a comment..."
          className="flex-1 px-3 py-2 border border-gray-300 rounded"
          value={newComment}
          onChange={(e) => setNewComment(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleAddComment()}
        />
        <button
          onClick={handleAddComment}
          className="px-4 py-2 bg-green-700 text-white rounded hover:bg-green-800"
        >
          Post
        </button>
      </div>
    </div>
  );
}
