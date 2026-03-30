import { useState } from "react";

function SprintActivityForm({ sprintId, activities, onSubmit }) {
  const [activityId, setActivityId] = useState("");
  const [days, setDays] = useState([]);

  const toggleDay = (day) => {
    setDays((prev) =>
      prev.includes(day)
        ? prev.filter((d) => d !== day)
        : [...prev, day]
    );
  };

  return (
    <div>
      <h3>Assign Activity</h3>

      <select onChange={(e) => setActivityId(e.target.value)}>
        <option>Select activity</option>
        {activities.map((a) => (
          <option key={a.id} value={a.id}>
            {a.name}
          </option>
        ))}
      </select>

      <div>
        {["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].map(day => (
          <label key={day}>
            <input
              type="checkbox"
              onChange={() => toggleDay(day)}
            />
            {day}
          </label>
        ))}
      </div>

      <button onClick={() => onSubmit(sprintId, activityId, days)}>
        Add
      </button>
    </div>
  );
}

export default SprintActivityForm;