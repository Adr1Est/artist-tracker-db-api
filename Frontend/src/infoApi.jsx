export const getArtists = () => {
  const url = `http://localhost:5000/artists`;

  return fetch(url)
    .then((res) => res.json())
    .then((data) => data);
};
