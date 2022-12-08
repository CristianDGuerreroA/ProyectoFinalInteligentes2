import React, { useState, useEffect } from "react";
import axios from "axios";
import carta from "./carta.jpg"

import "./App.css";

const endpoint = "http://127.0.0.1:8000/upload-file/";

function App() {
  const [selectedCard, setSelectedCard] = useState("");
  const [image, setImage] = useState("");
  const [name, setName] = useState("");
  const [percentaje, setPersentaje] = useState("");

  useEffect(() => {
    setSelectedCard(carta);
  },[]);

  const onImageChange = (event) => {
    if (event.target.files && event.target.files[0]) {
      setImage(event.target.files[0]);
      setSelectedCard(URL.createObjectURL(event.target.files[0]));
    }
  };

  const predict = async (e) => {
    e.preventDefault();
    let formData = new FormData();
    formData.append('uploaded_file', image);

    const response = await axios.post(endpoint, formData);

    setName(response.data.Carta);
    setPersentaje(response.data.porcentaje);
  };


  return (
    <div className="m-2 md:m-10 p-2  md:p-10 bg-white rounded-3xl">
      <div className="md:grid md:grid-cols-2 md:gap-10">
        <div className="mt-5 md:col-start-1 pl-20">
          <img src={selectedCard} alt="Carta"/>
        </div>
        <div className="mt-5 md: col-start-2 md:mt-0">
          <form className="w-full max-w-sm " onSubmit={predict}>
            <div className="flex items-center border-b border-teal-500 py-2 pt-20">
              <input
                className="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
                type="file"
                accept="image/png, image/gif, image/jpeg"
                aria-label="imagen"
                onChange={onImageChange}
              />
              <button
                className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
                type="submit"
              >
                Usar
              </button>
            </div>
          </form>
        </div>
        <div>
          Procentaje = {percentaje}
        </div>
        <div>
          Nombre = {name}
        </div>
      </div>
    </div>
  );
}

export default App;
