import { apiFetch } from "./apiClient";

export function addActivityToSprint(sprintId, payload) {
    return apiFetch(`/sprint-weeks/${sprintId}/activities`, {
        method: "POST",
        body: JSON.stringify(payload),
    });
}

export function getSprintActivities(sprintId) {
    return apiFetch(`/sprint-weeks/${sprintId}/activities`);
}   