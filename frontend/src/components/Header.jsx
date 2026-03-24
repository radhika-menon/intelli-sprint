import React from "react";
import "../App.css"; // adjust if using dedicated CSS module for header

function Header() {
  return (
    <section id="header">
      <div id="docs">
        <svg className="icon" role="presentation" aria-hidden="true">
          <use href="/icons.svg#documentation-icon"></use>
        </svg>
        <h3>IntelliSprint</h3>
      </div>
        
    </section>
  );
}

export default Header;
