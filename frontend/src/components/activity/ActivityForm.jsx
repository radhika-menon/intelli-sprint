import { useState } from "react";

function ActivityForm({ onCreate }) {
    const [name, setName] = useState("");

    const handleSubmit = async () => {
        if (!name) return;
        await onCreate(name);
        setName("");
    };

    return (
        <div>
            <h3>Create Activity</h3>
            <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Enter activity name"
            />
            <button onClick={handleSubmit}>Add</button>
        </div>
    );
}

export default ActivityForm;