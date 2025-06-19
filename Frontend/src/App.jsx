import './App.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faHeart, faHeartCrack, faHouse, faMusic } from '@fortawesome/free-solid-svg-icons'
import Header from './Components/Header.jsx'
import ListsRenderComponent from './Components/ListsRenderComponent.jsx'

library.add(faHouse, faMusic, faHeart, faHeartCrack)

function App() {

  return (
    <>
      <Header />
      <ListsRenderComponent />
    </>
  )
}

export default App
