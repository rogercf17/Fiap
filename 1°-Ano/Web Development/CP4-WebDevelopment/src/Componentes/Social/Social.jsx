import Cards from "../Cards/Cards";

function Social({ social }) {

    const info = [
        {
            number: '01',
            title: 'Youtube',
            description: 'Produza conteúdo cativante e conquiste seu público com vídeos de altíssima qualidade no maior palco digital do mundo.',
            anonymous: true,
            backgroundColor: "pink",
            platformIcon: '/youtube-icon.png',
        },
        {
            number: '02',
            title: 'Tiktok',
            description: 'Faça sua criatividade brilhar em vídeos curtos e envolventes que vão cativar a comunidade global do TikTok.',
            anonymous: true,
            backgroundColor: "rgba(255, 255, 0, 0.5)",
            platformIcon: '/tiktok-icon.png',
        },
        {
            number: '03',
            title: 'Facebook',
            description: 'Conecte-se com sua audiência de forma autêntica e impactante através de vídeos que se destacam no feed do Facebook.',
            anonymous: true,
            backgroundColor: "rgb(173, 216, 230, 0.5)",
            platformIcon: '/facebook-icon.png',

        },
        {
            number: '04',
            title: 'Instagram',
            description: 'Compartilhe suas histórias de maneira única e conquiste milhões de likes no Instagram utilizando Stories e Reels.',
            anonymous: true,
            backgroundColor: "rgb(0, 0, 139, 0.5)",
            platformIcon: '/instagram-icon.png',

        }
    ]
    return (
        <div className="Social">
            <Cards dados={info} />
        </div>
    );
}

export default Social;
