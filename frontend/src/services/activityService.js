import { apiFetch } from "./apiClient";

export function createActivity(name) {
    return apiFetch("/activities", {
        method: "POST",
        body: JSON.stringify({ name }),
    });
}

export function getActivities() {
    return apiFetch("/activities");
}   