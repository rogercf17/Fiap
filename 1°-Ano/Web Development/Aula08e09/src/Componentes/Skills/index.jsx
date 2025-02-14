import Card from "../Card";

function Skills({ skills }) {
  const habilidades = [
    {
      titulo: "HTML",
      nivel: "Avançado",
      tempo: "2 anos",
      color: "orange"
    },
    {
      titulo: "CSS",
      nivel: "Avançado",
      tempo: "2 anos",
      color: "blue"
    },
    {
      titulo: "Javascript",
      nivel: "Intermediário",
      tempo: "1 ano",
      color: "yellow"
    },
    {
      titulo: "React",
      nivel: "Básico",
      tempo: "1 mês",
      color: "cyan"
    },
    {
      titulo: "Python",
      nivel: "Intermediário",
      tempo: "1 ano",
      color: "green"
    },
    {
      titulo: "Node Js",
      nivel: "Intermediário",
      tempo: "1 ano1",
      color: "green"
    }
  ]
  return (
    <div className="skills">
      <h2>Habilidades</h2>
      <Card dados={habilidades} />
      {/* <Card titulo="CSS" nivel="Avançado" tempo="2 anos"/>
      <Card titulo="HTML" nivel="Avançado" tempo="2 anos"/>
      <Card titulo="Javascript" nivel="Intermediário" tempo="1 ano"/> */}
    </div>
  );
}

export default Skills;