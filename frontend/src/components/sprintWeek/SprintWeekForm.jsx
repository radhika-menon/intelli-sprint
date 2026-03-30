import { useState } from "react";

function SprintWeekForm({ onCreate }) {
  const [date, setDate] = useState("");
  const [week, setWeek] = useState("");

  return (
    <div>
      <h3>Create Sprint Week</h3>
      <input type="date" onChange={(e) => setDate(e.target.value)} />
      <input type="number" onChange={(e) => setWeek(e.target.value)} />
      <button onClick={() => onCreate(date, week)}>Create</button>
    </div>
  );
}

export default SprintWeekForm;