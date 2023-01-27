import styled from "styled-components";
import { COLORS } from "./Colors";

const Section = styled.div`
    margin: 1em;
    padding: 1em;
    min-height: 200px;
    border-radius: 4px;
    // border: 1px solid ${COLORS.primary};
    background: ${COLORS.dark};
    box-shadow: 0px 1px 5px #000;
`;

export default Section;
