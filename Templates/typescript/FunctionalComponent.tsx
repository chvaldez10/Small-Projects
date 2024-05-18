import React from "react";

interface FunctionalComponentProps {
  title: string;
  flag: boolean;
}

const FunctionalComponent: React.FC<FunctionalComponentProps> = ({
  title,
  flag,
}) => {
  return (
    <div>
      <h1>{title}</h1>
      {flag && <p>The flag is true!</p>}
    </div>
  );
};

export default FunctionalComponent;
