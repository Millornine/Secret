"use client";
import Image from "next/image";
import { useState, useEffect } from "react";
import Modal from './components/modals';

export default function Home() {
  const [currentPage, SetCurrentPage] = useState(1);
  const [Search, SetSearch] = useState("");
  const [SearchTemp, SetSearchTemp] = useState("");
  const [loading, setLoading] = useState(false);
  const [hasMore, setHasMore] = useState(false);
  const [DataUnSplash, SetData] = useState([]);
  const [Error, setError] = useState("");
  const [modalOpen, setModalOpen] = useState(false);
  const [selectedImage, setSelectedImage] = useState({ url: '', alt: '' });
  const acc_key = "JJXiKAaJjWY2ahdAcBfp2Z9kmTqAIupMVfbAfRjD0wQ";

  const handleSubmit = async (e) => {
    if (e) e.preventDefault();
    SetSearchTemp(Search);

    try {
      setLoading(true);
      const res = await fetch(`https://api.unsplash.com/search/photos?page=${currentPage}&query=${Search}&per_page=8&lang=th`, {
        method: "GET",
        headers: { 
          "Authorization": `Client-ID ${acc_key}`
        }
      });

      if (res.ok) {
        const data = await res.json();
        if (data.results.length > 0) {
          if(currentPage > 1) {
            SetData((prevData) => [...prevData, ...data.results]);
          } else {
            SetData(data.results);
          }
          setHasMore(data.results.length > 0);
          setError("");
        } else {
          setHasMore(false); // No more results
          setError("No images found from this keyword "+ Search);
        }
      } else {
        setError("Failed to Fetch Data");
      }
    } catch (error) {
      setError("Network Error: Unable to Fetch Data");
    }
    setLoading(false);
  };

  const loadMore = () => {
    if (hasMore && !loading) {
      SetCurrentPage((prevPage) => prevPage + 1);
    }
  };

  useEffect(() => {
    if (currentPage > 1) {
      handleSubmit();
    }
  }, [currentPage]);

  useEffect(() => {
    if (Search != SearchTemp) {
      setHasMore(false);
    }
  }, [Search]);

  const openModal = (url, alt) => {
    setSelectedImage({ url, alt });
    setModalOpen(true);
  };

  const closeModal = () => {
    setModalOpen(false);
    setSelectedImage({ url: '', alt: '' });
  };

  return (
      <div className="text-center items-center justify-center mx-auto md:h-screen lg:py-0">
          <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
            <p className="text-center text-4xl font-bold leading-tight tracking-tight text-gray-900 md:text-4xl dark:text-white">
              Unsplash Services
            </p>

            <form className="max-w-lg mx-auto" onSubmit={handleSubmit}>
              <div className="relative">
                <input
                  type="search"
                  maxLength={30}
                  id="default-search"
                  className="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="ค้นหา ...."
                  required
                  value={Search}
                  onChange={(e) => SetSearch(e.target.value)}
                />
                <button
                  type="submit"
                  className="text-white absolute end-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                >
                  ค้นหา
                </button>
              </div>
            </form>
          </div>
        <div className="flex flex-wrap gap-5 text-center justify-center">
          {Error && (
            <p className="text-center text-4xl font-bold leading-tight tracking-tight text-gray-900 md:text-4xl dark:text-white">
              {Error}
            </p>
          )}
          {DataUnSplash.map((item) => (
            <div
              key={item.id}
              className="relative w-80 h-96 overflow-hidden cursor-pointer"
              onClick={() => openModal(item.urls.full, item.alt_description)}
            >
              <Image
                src={item.urls.small}
                alt={item.alt_description}
                layout="fill"
                objectFit="cover"
              />
            </div>
          ))}
        </div>
        {loading && <p className="text-center py-4">Loading...</p>}
        {hasMore && !loading && (
          <button
            type="button"
            className="mt-6 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
            onClick={loadMore}
          >
            แสดงเพิ่มเติม
          </button>
        )}
        <Modal
          isOpen={modalOpen}
          onClose={closeModal}
          imageUrl={selectedImage.url}
          altText={selectedImage.alt}
        />
      </div>
  );
}
