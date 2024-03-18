axios ({
    url: 'http://127.0.0.1:5000/parse',
    method: 'GET',
    params: {
        filename: 'README'
    }
}).then(result => {
    const mdContext = document.querySelector('.mdContext')
    mdContext.innerHTML = result.data
}).catch(err => {
    console.log(err)
})

