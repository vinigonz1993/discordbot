import React, { useEffect, useState } from "react";
import { Row, Col } from "react-bootstrap";
import Section from "./common/Section";
import Api from './requests';

const Main = () => {
    const [routes, setRoutes] = useState<[]>([]);
    useEffect(() => {
        Api.oct.get().then(
            (response) => setRoutes(response.data['GetRouteSummaryForStopResult']['Routes']['Route']),
        );
    }, []);

    return (
        <>
            <h6>ToolBoxAPIs</h6>
            <hr />
            <Row>
                <Col xl={6} lg={6} md={6} sm={12}>
                    <Section>
                        OCTranstpo
                        <hr/>
                        {routes.map((route) => (
                            <>
                                <h6>{route['RouteNo']} - {route['RouteHeading']}</h6>
                            </>
                        ))}
                    </Section>
                </Col>
                <Col xl={4} lg={6} md={6} sm={12}>
                    <Section>
                        Currencies
                    </Section>
                </Col>
                <Col xl={4} lg={6} md={6} sm={12}>
                    <Section>
                        Currencies
                    </Section>
                </Col>
            </Row>
        </>
    );
};

export default Main;
