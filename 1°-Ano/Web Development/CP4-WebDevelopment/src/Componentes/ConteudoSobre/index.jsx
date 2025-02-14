export default function ConteudoSobre() {
    return (
        <>
            <section id='hero-dois'>
                <div className="div-hero">
                    <h1>Bem-vindo à revolução dos vídeos!</h1>
                    <p>
                        Somos uma startup com o objetivo de facilitar a
                        produção de conteúdo em larga escala com qualidade profissional,
                        capaz de atingir uma audiência de milhões de seguidores.
                    </p>
                    <button className="button-hero">Baixe o app</button>
                </div>
                <img src="/celular.png" alt="Imagem do Hero" />
                <img src="/celular-dois.png" alt="Imagem do Hero" />
            </section>

            <section id="box-planos">
                <h2>Planos</h2>
                <div className="planos">
                    <div className="plano individual">
                        <div className="titulo"><h3>Individual</h3></div>
                        <div className="informacoes">
                            <p>1 Usuário</p>
                            <div>
                                <p>10 Vídeos <strong>R$15</strong></p>
                                <img src="/icon-seta.png" alt="Icone" height="15px" />
                            </div>
                        </div>
                        <button className="btn-plano">Cadastrar</button>
                    </div>

                    <div className="plano profissional">
                        <div className="titulo"><h3>Profissional - Times</h3></div>
                        <div className="informacoes">
                            <p>1-10 Usuários</p>
                            <div>
                                <p>Vídeos Ilimitados <strong>R$40</strong></p>
                                <img src="/icon-seta.png" alt="Icone" height="15px" />
                            </div>
                            <p>+10 Usuários</p>
                            <div>
                                <p>Vídeos Ilimitados <strong>R$20</strong></p>
                                <img src="/icon-seta.png" alt="Icone" height="15px" />
                            </div>

                        </div>
                        <button className="btn-plano">Cadastrar</button>
                    </div>

                    <div className="plano corporativo">
                        <div className="titulo"><h3>Corporativo</h3></div>
                        <div className="informacoes">
                            <img src="/icon-celular.png" height="110px" width="120px" alt="Imagem plano corporativo" className="icon-celular" />

                        </div>
                        <button className="btn-plano">Entre Em Contato</button>
                    </div>
                </div>
            </section>
        </>
    )
}