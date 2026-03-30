import { useState, useEffect } from 'react'
import './App.css'
import Header from './components/Header';
import Timer from './components/Timer';
import Stats from './components/Stats';
import SprintWeekForm from './components/sprintWeek/SprintWeekForm';
import SprintWeekList from './components/sprintWeek/SprintWeekList';
import ActivityForm from './components/activity/ActivityForm';
import ActivityList from './components/activity/ActivityList';
import SprintActivityForm from './components/sprintActivity/SprintActivityForm';
import { createSprintWeek, getSprintWeeks } from './services/sprintWeekService';
import { createActivity, getActivities } from './services/activityService';
import { addActivityToSprint, getSprintActivities } from './services/sprintActivityService';

function App() {
  const [count, setCount] = useState(0)

  const [activities, setActivities] = useState([]);
  const [sprintWeeks, setSprintWeeks] = useState([]);
  const [selectedSprint, setSelectedSprint] = useState(null);
  const [sprintActivities, setSprintActivities] = useState([]);

  // Load initial data
  useEffect(() => {
    async function loadData() {
      const activityData = await getActivities();
      setActivities(Array.isArray(activityData) ? activityData : []);
      const sprintData = await getSprintWeeks();
      setSprintWeeks(Array.isArray(sprintData) ? sprintData : []);
    }
    loadData();
  }, []);

  // Load sprint activities when sprint changes
  useEffect(() => {
    if (!selectedSprint) return;

    async function loadSprintData() {
      const data = await getSprintActivities(selectedSprint);
      setSprintActivities(data);
    }

    loadSprintData();
  }, [selectedSprint]);

  // Create activity
  const handleCreateActivity = async (name) => {
    const newActivity = await createActivity(name);

    // update UI immediately
    setActivities((prev) => [...prev, newActivity]);
  };

  // Create sprint week
  const handleCreateSprint = async (date, week) => {
    const newSprint = await createSprintWeek({
      week_start_date: date,
      semester_week: Number(week),
    });

    setSprintWeeks((prev) => [...prev, newSprint]);
  };

  // Assign activity
  const handleAssignActivity = async (sprintId, activityId, days) => {
    const res = await addActivityToSprint(sprintId, {
      activity_id: Number(activityId),
      days,
      status: "Planned",
    });

    setSprintActivities((prev) => [...prev, ...res]);
  };

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
          <div style={{ display: "flex", gap: "20px" }}>

            {/* LEFT: Activities */}
            <div>
              <h2>Activities</h2>
              <ActivityForm onCreate={handleCreateActivity} />
              <ActivityList activities={activities} />
            </div>

            {/* MIDDLE: Sprint Weeks */}
            <div>
              <h2>Sprint Weeks</h2>
              <SprintWeekForm onCreate={handleCreateSprint} />
              <SprintWeekList
                sprintWeeks={sprintWeeks}
                onSelect={setSelectedSprint}
              />
            </div>

            {/* RIGHT: Sprint Planner */}
            <div>
              <h2>Sprint Planner</h2>

              {selectedSprint && (
                <>
                  <SprintActivityForm
                    sprintId={selectedSprint}
                    activities={activities}
                    onSubmit={handleAssignActivity}
                  />

                  <div>
                    <h3>Planned Activities</h3>
                    {sprintActivities.map((sa) => (
                      <div key={sa.id}>
                        Activity {sa.activity_id} - {sa.day}
                      </div>
                    ))}
                  </div>
                </>
              )}
            </div>
          </div>

        </div>

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
