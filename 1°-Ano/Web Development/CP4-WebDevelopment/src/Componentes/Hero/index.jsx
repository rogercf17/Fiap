import PropTypes from 'prop-types';
export default function Hero(props) {
    return(
        <>
            <section id="hero">
                {/* <div className="div-hero">
                    <h1>Crie seus vídeos online</h1>
                    <p>
                        Transforme suas ideias em filmes memoráveis: 
                        onde a criatividade<br /> encontra a simplicidade.
                    </p>
                    <button className="button-hero">Começar Agora</button>
                </div>
                <img src="/Hero-image.png" alt="Imagem do Hero"  /> */}
                <div className="div-hero">
                    <h1>{props.titulo}</h1>
                    <p>
                        {props.paragrafo}
                    </p>
                    <button className="button-hero">{props.legenda}</button>
                </div>
            </section>
        </>
    )
}
Hero.propTypes = {
    titulo: PropTypes.string.isRequired,
    paragrafo: PropTypes.string.isRequired,
    legenda: PropTypes.string.isRequired,
    imagem: PropTypes.string.isRequired
};