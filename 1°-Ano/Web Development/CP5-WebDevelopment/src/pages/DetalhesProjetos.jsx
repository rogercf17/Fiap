import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { projetos } from "../data/projetosData";

export default function DetalhesProjetos() {
    const { id } = useParams();
    const projeto = projetos.find(p => p.id === parseInt(id));

    if (!projeto) {
        return <div className="text-white">Projeto não encontrado</div>;
    }

    return (
        <div className="w-10/12 mx-auto mt-10 mb-10">
            <Link to="/projetos" className="text-blue-500 hover:underline mb-4 inline-block">&larr; Voltar para Projetos</Link>
            <div className="bg-gray-800 p-6 rounded-lg shadow-lg">
                <img src={projeto.capa} alt={projeto.titulo} className="w-full h-64 object-cover rounded-md mb-6" />
                <h1 className="text-white text-3xl font-bold mb-4">{projeto.titulo}</h1>
                <p className="text-gray-300 mb-6">{projeto.descricao}</p>
                <div className="mb-6">
                    <h2 className="text-white text-xl font-semibold mb-2">Tecnologias utilizadas:</h2>
                    <div className="flex flex-wrap gap-2">
                        {projeto.tecnologias.map((tec, index) => (
                            <span 
                                key={index} 
                                className="bg-blue-600 text-white px-3 py-1 rounded-full text-sm"
                            >
                                {tec}
                            </span>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
}