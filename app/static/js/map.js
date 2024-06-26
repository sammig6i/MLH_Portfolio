


var map = L.map("map-id").setView([38.5, -98], 3);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "© OpenStreetMap contributors",
}).addTo(map);

function addMarker(lat, lng, place, imageURL) {
  L.marker([lat, lng])
    .addTo(map)
    .bindPopup(
      `<b>${place}</b><br><img src="${imageURL}" alt="${place}" width="100"><br>${place}`
    )
    .openPopup();
}

addMarker(
  43.615,
  -116.2023,
  "Boise, Idaho",
  "https://images.unsplash.com/photo-1465244554671-e501f19a3bb3?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
);
addMarker(
  34.0522,
  -118.2437,
  "Los Angeles, CA",
  "https://images.unsplash.com/photo-1528041119984-da3a9f8d04d1?q=80&w=1409&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
);
addMarker(
  34.1083,
  -117.2898,
  "San Bernardino County, CA",
  "https://images.unsplash.com/photo-1459258350879-34886319a3c9?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHJpYWx0byUyMGNhbGlmb3JuaWF8ZW58MHx8MHx8fDA%3D"
);
addMarker(
  32.7157,
  -117.1611,
  "San Diego, CA",
  "https://images.unsplash.com/photo-1553191657-2e1685c0b5d3?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8c2FuJTIwZGllZ28lMjBjYWxpZm9ybmlhfGVufDB8fDB8fHww"
);
addMarker(
  28.5383,
  -81.3792,
  "Orlando, Florida",
  "https://images.unsplash.com/photo-1597466599360-3b9775841aec?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZGlzbmV5JTIwd29ybGR8ZW58MHx8MHx8fDA%3D"
);
addMarker(
  47.6062,
  -122.3321,
  "Seattle, WA",
  "https://images.unsplash.com/photo-1534450539339-6d1c81ad18e2?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8ZGlzbmV5JTIwd29ybGR8ZW58MHx8MHx8fDA%3D"
);
addMarker(
  40.7608,
  -111.891,
  "SLC, Utah",
  "https://images.unsplash.com/photo-1493929491462-1a3ecca63007?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8c2FsdCUyMGxha2UlMjBjaXR5JTIwdXRhaHxlbnwwfHwwfHx8MA%3D%3D"
);
addMarker(
  39.5296,
  -119.8138,
  "Nevada",
  "https://images.unsplash.com/photo-1605833556294-ea5c7a74f57d?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bGFzJTIwdmVnYXN8ZW58MHx8MHx8fDA%3D"
);
addMarker(
  44.0,
  -120.5,
  "Oregon",
  "https://images.unsplash.com/photo-1537118169787-d32386cdd0a8?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8b3JlZ29ufGVufDB8fDB8fHww"
);
addMarker(
  34.0489,
  -111.0937,
  "Arizona",
  "https://plus.unsplash.com/premium_photo-1675826774820-5fa779f5256a?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8YXJpem9uYXxlbnwwfHwwfHx8MA%3D%3D"
);
addMarker(
  46.8797,
  -110.3626,
  "Montana",
  "https://plus.unsplash.com/premium_photo-1688429242520-b88107a0e5eb?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bW9udGFuYXxlbnwwfHwwfHx8MA%3D%3D"
);
addMarker(
  20.7967,
  -156.3319,
  "Hawaii",
  "https://images.unsplash.com/photo-1713992852903-d8d78192e16e?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8aG9ub2x1bHUlMjBoYXdhaWl8ZW58MHx8MHx8fDA%3D"
);