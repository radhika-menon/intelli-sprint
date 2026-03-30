import { apiFetch } from "./apiClient";

export function createSprintWeek(data) {
    return apiFetch("/sprint-weeks", {
        method: "POST",
        body: JSON.stringify(data),
    });
}

export function getSprintWeeks() {
    return apiFetch("/sprint-weeks");
}   