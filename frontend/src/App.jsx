import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Header from './components/Header';
import Timer from './components/Timer';
import Stats from './components/Stats';
import SprintPlan from './components/SprintPlan'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Header />
      <div className="ticks"></div>

      <section id="next-steps">
        <Stats />
        <Timer />
      </section>
      <div className="ticks"></div>
      <section id="spacer"></section>

      <div className="ticks"></div>

      <section id="center">

        <div>
          <h1>Planned Sprint</h1>
          
        </div>
        <button
          className="counter"
          onClick={() => setCount((count) => count + 1)}
        >
          Count is {count}
        </button>
      </section>

      <section id="next-steps">
        <div id="docs">
          <h2>Motivate Me!</h2>
          <form>
            <input type="text" placeholder="Enter a message to motivate yourself" />
            <button type="submit">Submit</button>
          </form>
        </div>
        <div id="social">

          <h2>Time Capsule</h2>
          <p>This feature is in progress</p>
          
        </div>
      </section>

      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App
