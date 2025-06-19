import Card from "./Card";
import "./Card.css"

const CardList = ({strategy, title, tag }) => {
  return strategy({title, tag});
};

export default CardList;
