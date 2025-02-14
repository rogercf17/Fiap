import CardProjetos from "../componentes/CardProjetos";
import { projetos } from "../data/projetosData";

export default function Projetos() {
    return (
        <section className="w-10/12 h-fit flex flex-col mx-auto justify-center items-center mb-10">
            <h1 className="text-white text-3xl text-center mb-8">Meus Projetos</h1>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {projetos.map((projeto) => (
                <CardProjetos 
                    key={projeto.id}
                    id={projeto.id}
                    titulo={projeto.titulo}
                    capa={projeto.capa}
                    descricao={projeto.descricao}
                    tecnologias={projeto.tecnologias}
                />
            ))}
            </div>
        </section>
    );
}
