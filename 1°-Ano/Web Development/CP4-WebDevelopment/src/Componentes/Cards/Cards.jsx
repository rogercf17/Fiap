export default function Cards({ dados }) {
    /*console.log(props)*/

    return (
        <>
            {
                dados.map((pegaDados, index) => (
                    <div
                        className="card"
                        key={index}
                        style={
                            {
                                color: pegaDados.color,
                                backgroundColor: pegaDados.backgroundColor
                            }
                        }
                    >
                        <div className="card-header">
                            <h1 id="nb">{pegaDados.number}</h1>
                            <img
                                src={pegaDados.platformIcon}
                                alt={`${pegaDados.title} icon`}
                                style={{ width: '30px', height: '30px', marginTop: '-50px' }}
                            />
                        </div>
                        <h3>{pegaDados.title}</h3>
                        <p>{pegaDados.description}</p>
                        <a href={pegaDados.linkCard}>{pegaDados.titulo} </a>
                    </div>
                ))
            }
        </>
    );

}

/*const {titulo, nivel, tempoxp} = props ---- quebra de props
        

*/