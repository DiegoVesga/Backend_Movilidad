/*pk.eyJ1IjoiamFjb25ldCIsImEiOiJjbG5ybW8xZzQwMThuMmxwcTUwZHZmaHJiIn0.oWoK3TLG9tupXEkuMrjyeA*/

mapboxgl.accessToken = 'pk.eyJ1IjoiamFjb25ldCIsImEiOiJjbG5ybW8xZzQwMThuMmxwcTUwZHZmaHJiIn0.oWoK3TLG9tupXEkuMrjyeA'
let map = new mapboxgl.map(

    {
        container: 'pruebamapa',
        style:'mapbox://styles/mapbox/streets-v11',
        center:[-74.806984,11.004107],
        zoom:15
    }
)