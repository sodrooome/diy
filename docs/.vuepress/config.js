module.exports = {

    title: 'Do It Yourself Framework',
    description: 'A Python Web Framework for learning purposes only',
    themeConfig: {

        repo: "https://github.com/sodrooome/diy",
        repoLabel: "Contribute",

        editLinkText: "Caught a mistake? Edit this page on github",

        activeHeaderLinks: false,

        serviceWorker: {

            updatePopup: {

                message: "New content is up",
                buttonText: "Refresh"

            }

        },

        nav: [

            { text: 'Home', link: '/'},
            { text: 'Index', link: '/index/'},
            { text: 'Reference', link: '/reference/'},
            { text: 'Story', link: '/story/'}

        ],

        sidebar: [

            '/',
            '/index/',
            '/reference/',
            '/setting/',
            '/how-to/',
            '/story/'


        ]

    }

}