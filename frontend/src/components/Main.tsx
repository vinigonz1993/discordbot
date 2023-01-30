import React from "react";
import { Row, Col } from "react-bootstrap";
import styled from "styled-components";
import Section from "./common/Section";
import OCT from "./OCT";

const Container = styled.div`
    margin-left: 250px;
`;

const Main = () => {
    return (
        <Container>
            <h6>ToolBoxAPIs</h6>
            <hr />
            <Row>
                <Col xl={6} lg={12} md={12} sm={12}>
                    <Section>
                        OCTranstpo
                        <hr/>
                        <OCT />
                    </Section>
                </Col>
                <Col xl={6} lg={6} md={6} sm={12}>
                    <Section>
                        ChatGPT
                        <hr />
                        Coming soon
                    </Section>
                </Col>
                <Col xl={6} lg={6} md={6} sm={12}>
                    <Section>
                        Currencies
                        <hr />
                        Coming soon
                    </Section>
                </Col>
                <Col xl={6} lg={6} md={6} sm={12}>
                    <Section>
                        Quotes
                        <hr />
                        Coming soon
                    </Section>
                </Col>
            </Row>
        </Container>
    );
};

export default Main;
