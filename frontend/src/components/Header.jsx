import React from "react";
import "../App.css";

function Header() {
  return (
    <section id="header">
      <div id="docs">
        <svg className="icon" role="presentation" aria-hidden="true">
          <use href="/icons.svg#documentation-icon"></use>
        </svg>
        <h3>SprintAWeek</h3>
      </div>

    </section>
  );
}

export default Header;
