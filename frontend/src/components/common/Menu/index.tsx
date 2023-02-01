import styled from "styled-components";
import { COLORS } from "../Colors";
import { Link, Route, Routes } from "react-router-dom";

const Container = styled.div`
    z-index: 9999;
    padding: 0 !important;
    background: ${COLORS.secondary};
    left: 0 !important;
    position: fixed;
    height: 100vh !important;
    border-right: 6px solid ${COLORS.border};
    width: 250px !important;
`;

const UpperText = styled.h2`
    padding-top: 1em;
    padding-bottom: 1em;
    background: ${COLORS.dark};
    border-bottom: 6px solid ${COLORS.border};
`;

const ListContainer = styled.ul`
    padding: 0;
    margin: 0;
`;

const List = styled.li`
    list-style-type: none;
    transition: 0.35s;
    width: 100%;
    padding-top: 5px;
    padding-bottom: 5px;
`;

const LinkContainer = styled(Link)`
    text-decoration: none;
    color: ${COLORS.text.menu};

    &:hover {
        color: ${COLORS.light};
        font-weight: bold;
    }
`;

const Menu = () => (
    <Container>
    <UpperText>ToolBoxAPIs</UpperText>
    <ListContainer>
        <List>
            <LinkContainer to="/">Main</LinkContainer>
        </List>
        <List>
            <LinkContainer to="/o">OCTranspo API</LinkContainer>
        </List>
        <List>
            <LinkContainer to="/o">ChatGPT API</LinkContainer>
        </List>
        <List>
            <LinkContainer to="/o">Currency API</LinkContainer>
        </List>
        <List>
            <LinkContainer to="/o">Quotes API</LinkContainer>
        </List>
    </ListContainer>
    </Container>
)

export default Menu;
