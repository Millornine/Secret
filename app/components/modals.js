import React from 'react';

const Modal = ({ isOpen, onClose, imageUrl, altText }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50">
      <div className="relative max-w-screen-sm mx-4">
        <button
          onClick={onClose}
          className="absolute top-4 right-4 text-white text-2xl "
        >
          &times;
        </button>
        <img
          src={imageUrl}
          alt={altText}
          className="w-full h-auto object-contain w-[500px] h-96"
        />
      </div>
    </div>
  );
};

export default Modal;