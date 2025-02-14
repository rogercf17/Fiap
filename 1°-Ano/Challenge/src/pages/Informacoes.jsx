import CardCorridas from "../componentes/CardCorridas"

export default function Informacoes() {
  return (
    <section
      className="
        w-10/12
        flex flex-col
        justify-center items-center	mx-auto
        flex-grow
        pb-14
        gap-4
    "
    >
      <div
        className="
        mt-2.5 p-3
        rounded-2xl
        w-full
      "
      >
        <h1 className="font-bold antialiased text-4xl mb-1.5">História</h1>
        <p className="text-base text-justify leading-6">
          O campeonato de Fórmula E (Fórmula E) foi concebido em 2011 como uma
          alternativa sustentável e ambientalmente amigável às corridas
          tradicionais de rodas abertas. A ideia era criar uma plataforma para
          veículos elétricos competirem em uma série de corridas de alto nível,
          promovendo a inovação e o desenvolvimento na mobilidade eletrônica.
          Após vários anos de planejamento e desenvolvimento, a primeira corrida
          de Fórmula E ocorreu em 13 de setembro de 2014, em Pequim, China, com
          o apoio da Fédération Internationale de lucitaAutomobile (FIA).
        </p>
        <h2 className="font-bold text-xl my-1">
          Primeira Temporada e Crescimento
        </h2>
        <p className="text-base text-justify leading-6">
          A temporada inaugural contou com 20 pilotos de 10 equipes, com Audi
          Sport ABT Schaeffler e Andretti Autosport sendo duas das equipes de
          destaque. O piloto brasileiro Lucas di Grassi venceu a primeira
          corrida da Fórmula E, e o campeonato foi ganho por Nelson Piquet Jr.
          Desde então, a série cresceu, com cada temporada introduzindo novas
          equipes, pilotos e tecnologias.
        </p>
        <h2 className="font-bold text-xl my-1">Principais Marcos</h2>
        <ul className="list-disc px-5">
          <li>
            2015: A Fórmula E se expande para 11 cidades, com a adição de Miami
            e Long Beach.
          </li>
          <li>
            2016: O campeonato apresenta o seu primeiro evento de duas cabeças
            em Londres.
          </li>
          <li>
            2017: A Fórmula E celebra a sua 50a corrida eletrónica e introduz o
            sistema “FanBoost”, permitindo aos fãs votar nos seus pilotos
            favoritos.
          </li>
          <li>
            2018: A série atinge um marco de 100 corridas eletrónicas e introduz
            o sistema “Attack Mode”, permitindo que os condutores aumentem
            temporariamente a sua potência.
          </li>
          <li>
            2020: A Fórmula E se torna o Campeonato Mundial de Fórmula E da FIA,
            com a introdução de um novo sistema de pontos e um calendário
            revisado.
          </li>
        </ul>
        <button className="mt-5 bg-teal-500 w-40 h-10 rounded-full text-black hover:opacity-70">Descubra mais</button>
      </div>
      <div className="
        mt-2.5 p-3
        rounded-2xl
        w-full
      ">
        <h1 className="font-bold antialiased text-4xl mb-1.5">Sustentabilidade</h1>
        <p className="text-base text-justify leading-6">
          Na Fórmula E, aspiramos acelerar a mudança rumo a um futuro elétrico,
          uma corrida e uma cidade de cada vez. Utilizando o espetáculo do
          desporto, estamos a enviar uma mensagem poderosa e significativa para
          ajudar a alterar as perceções e acelerar a transição para a mobilidade
          elétrica. Também operamos como um banco de testes para impulsionar o
          desenvolvimento de novas tecnologias necessárias para um futuro
          elétrico e de baixo carbono. Trabalhando em estreita colaboração com
          as cidades-sede para deixar um legado duradouro onde quer que
          compitamos, a Fórmula E corre por um futuro mais limpo e mais rápido.
          A nossa política de sustentabilidade orienta a forma como trabalhamos
          e as ações que tomamos, definindo os nossos valores e objetivos para
          garantir que o nosso evento seja o mais sustentável possível.
        </p>
        <button className="mt-5 bg-teal-500 w-40 h-10 rounded-full text-black hover:opacity-70">Política Formula E</button>
      </div>
      <div className="
        mt-2.5 p-3
        rounded-2xl
        w-full
        flex flex-col justify-around
      ">
        <h1 className="font-bold antialiased text-4xl mb-1.5">Calendário de corridas temp.24/25</h1>
        <div className="flex gap-20 items-center">
          <CardCorridas dia="07" mes="Dez" imagem="https://static-files.formula-e.pulselive.com/flags/br.svg" cidade="São Paulo" round="1" />
          <CardCorridas dia="11" mes="Jan" imagem="https://static-files.formula-e.pulselive.com/flags/mx.svg" cidade="Cidade do México" round="2" />
          <CardCorridas dia="14" mes="Jan" imagem="https://static-files.formula-e.pulselive.com/flags/sa.svg" cidade="Jeddah" round="3" />
          <CardCorridas dia="15" mes="Fev" imagem="https://static-files.formula-e.pulselive.com/flags/sa.svg" cidade="Jeddah" round="4" />
        </div>
      </div>
    </section>
  );
}
