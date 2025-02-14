import Roger from "/minha-Foto.png"
import CardSkills from "../componentes/CardSkills";

export default function Sobre() {
  return (
    <section className="
        w-full h-fit
        flex flex-col justify-center items-center gap-8
        mb-10
        mx-auto
        md:w-11/12
    ">
        <div className="flex flex-col items-center md:flex-row md:justify-evenly md:items-center">
          <img src={Roger} alt="Minha Foto" className="w-40 h-40 rounded-full md:w-80 md:h-80" />
          <p className="text-white text-justify text-base w-full px-5 mt-4 md:w-1/4 md:text-md md:text-white md:font-normal md:tracking-wider md:first-letter:text-3xl">
              Olá meu nome é Roger Cardoso Ferreira, tenho 19 anos e sou Engenheiro de Software. 
              Atualmente morando no bairro Jardim Grimaldi em São Paulo. Conclui meu ensino médio 
              integrado com o técnico em Análise de Desenvolvimentos de Sistemas na Etec Professor
              Camargo Aranha em 2020 e Agora estou cursando Engenharia de Software na FIAP.
              Gosto de musculação, jogar bola, tocar violão, aprender coisas novas e passar o tempo livre
              com meus amigos e familiares.
          </p>
        </div>
        <CardSkills />
    </section>
  );
}
