import styled from "styled-components";
import { COLORS } from "../Colors";

const Input = styled.input`
    border-radius: 2px;
    height: 20px;
    background: ${COLORS.dark};
    color: #fff;
    border: 1px solid ${COLORS.primary};
    padding: 10px;
    padding-left: 10px;
    padding-right: 10px;
    font-size: 0.7em;
`;

export default Input;
