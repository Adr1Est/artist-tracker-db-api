import { getArtists } from "../infoApi";

export const getArtistsData = async() =>{
    const data = await getArtists();
    return data;
}

      