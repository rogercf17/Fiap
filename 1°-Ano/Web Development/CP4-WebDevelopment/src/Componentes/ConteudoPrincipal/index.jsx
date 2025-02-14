import Social from "../Social/Social";

export default function ConteudoPrincipal() {
    return (
        <>
            <section id="hero">
                <div className="div-hero">
                    <h1>Crie seus vídeos online</h1>
                    <p>
                        Transforme suas ideias em filmes memoráveis:
                        onde a criatividade<br /> encontra a simplicidade.
                    </p>
                    <button className="button-hero">Começar Agora</button>
                </div>
                <img src="/Hero-image.png" alt='Imagem do Hero' />
            </section>
            <section>
                <Social />
            </section>
        </>
    )
}