export default function ConteudoContato() {
    return(
        <>
            <div className="content">
                <div className="left-side">
                    <h1>Dúvidas e suporte, entre em contato:</h1>
                    <div className="social-icons">
                        <img src="/twitter.png" alt="Twitter" className="icon" />
                        <img src="/instagram.png" alt="Instagram" className="icon" />
                        <img src="/discord.png" alt="Discord" className="icon" />
                    </div>
                </div>
                <div className="right-side">
                    <form>
                        <div className="input-group">
                            <label htmlFor="nome">Nome:</label>
                            <input type="text" id="nome"/>
                        </div>
                        <div className="input-group">
                            <label htmlFor="email">E-mail:</label>
                            <input type="email" id="email"/>
                        </div>
                        <div className="input-group-textarea">
                            <label>Mensagem:</label>
                            <textarea></textarea>
                        </div>
                        <button type="submit" className="button-form">Enviar</button>
                    </form>
                </div>
            </div>
        </>
    )
}