function ActivityList({ activities, onSelect }) {
    return (
        <div>
            <h3>Activities</h3>
            {activities.map(a => (
                <div key={a.id} onClick={() => onSelect(a.id)}>
                    {a.name}
                </div>
            ))}
        </div>
    );
}

export default ActivityList;