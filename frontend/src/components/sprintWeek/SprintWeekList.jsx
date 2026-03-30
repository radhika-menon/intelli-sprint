function SprintWeekList({ sprintWeeks, onSelect }) {
    return (
        <div>
            <h3>Sprint Weeks</h3>
            {sprintWeeks.map(sw => (
                <div key={sw.id} onClick={() => onSelect(sw.id)}>
                    Week {sw.semester_week} - {sw.week_start_date}
                </div>
            ))}
        </div>
    );
}

export default SprintWeekList;