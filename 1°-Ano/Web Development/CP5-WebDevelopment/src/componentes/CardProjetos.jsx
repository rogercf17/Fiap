import { Link } from "react-router-dom"

export default function CardProjetos({ id, titulo, capa, descricao, tecnologias }) {
    return (
        <Link to={`/projetos/${id}`} className="block">
            <div className="bg-gray-800 p-4 rounded-lg shadow-lg h-96">
                <img src={capa} alt={titulo} className="w-full h-40 object-cover rounded-md mb-4" />
                <h2 className="text-white text-2xl font-bold mb-2">{titulo}</h2>
                <p className="text-gray-300 mb-4">{descricao}</p>
                <div className="flex flex-wrap gap-2">
                    {tecnologias.map((tec, index) => (
                        <span 
                            key={index} 
                            className="bg-blue-600 text-white px-2 py-1 rounded-full text-sm"
                        >
                            {tec}
                        </span>
                    ))}
                </div>
            </div>
        </Link>
    )
}
